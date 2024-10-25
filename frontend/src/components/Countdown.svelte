<script lang="ts">
	export let dayOfWeek: number; // 0 = Sunday, 1 = Monday, ..., 6 = Saturday
	export let times: string[] = ['09:00:00', '21:00:00']; // times in hh:mm:ss format
	export let durationHours: number = 1; // duration of each session in hours. floats are fine, e.g. 1.5 for 90 minutes
	import { format, addDays, addHours, addMinutes } from 'date-fns';
	import { zonedTimeToUtc, utcToZonedTime } from 'date-fns-tz';
	import { onDestroy, onMount } from 'svelte';

	/**
	 * @returns {{ isSessionRunning: true } | {isSessionRunning: false, countdownString: string}}
	 */
	function timeUntilNextSession() {
		const now = new Date();
		const TIMEZONE = 'America/New_York';
		/**
		 * @returns {Date}
		 */
		function getSessionTimestamp(
			etTimestamp: Date,
			time: string,
			targetDay?: number,
			duration: number,
			timezone = TIMEZONE
		) {
			const today = etTimestamp.getDay();
			const [hours, minutes] = time.split(':').map(Number);
			let sessionStart = new Date(
				etTimestamp.getFullYear(),
				etTimestamp.getMonth(),
				etTimestamp.getDate(),
				hours,
				minutes,
				0,
				0
			);
			const sessionEnd = new Date(sessionStart.getTime() + duration * 60 * 60 * 1000);
			const daysUntilNext = targetDay === undefined ? 0 : (targetDay - today + 7) % 7;
			const alreadyStarted = daysUntilNext === 0 && sessionStart.getTime() <= etTimestamp.getTime();
			const inProgress = alreadyStarted && etTimestamp.getTime() < sessionEnd.getTime();

			if (inProgress) {
				return { sessionStart, sessionInProgress: true };
			}

			if (daysUntilNext) {
				sessionStart = addDays(sessionStart, daysUntilNext);
			}

			if (alreadyStarted) {
				sessionStart = addDays(sessionStart, targetDay === undefined ? 1 : 7);
			}

			return { timestamp: sessionStart, sessionInProgress: false };
		}

		// Convert local time to Eastern Time (ET)
		const etTime = utcToZonedTime(now, TIMEZONE);

		// Get session start times
		/** @type {{ timestamp: Date, sessionInProgress: boolean }[]} */
		let sessions = times.map((time) => getSessionTimestamp(etTime, time, dayOfWeek, durationHours));

		// Check if any session is in progress currently
		const isInSession = sessions.some(({ sessionInProgress }) => sessionInProgress);

		if (isInSession) {
			return {
				isSessionRunning: true
			};
		}

		/** @type {number} - the time until the next session */
		const timeUntilNext = Math.min(
			...sessions.map(({ timestamp }) => timestamp.getTime() - etTime.getTime())
		);

		// Convert to hours, minutes, and seconds
		const days = Math.floor(timeUntilNext / (1000 * 60 * 60 * 24));
		const hours = Math.floor((timeUntilNext % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		const minutes = Math.floor((timeUntilNext % (1000 * 60 * 60)) / (1000 * 60));

		/**
		 * @param {number} d // days
		 * @param {number} h // hours
		 * @param {number} m // minutes
		 * @returns {string}
		 */
		function formatCountdownString(d: number, h: number, m: number): string {
			const parts: string[] = [];

			const addPart = (value: number, label: string) => {
				if (value > 0) {
					parts.push(`${value} ${label}${value !== 1 ? 's' : ''}`);
				}
			};

			addPart(d, 'day');
			addPart(h, 'hour');
			addPart(m, 'minute');

			if (parts.length === 0) {
				return 'Now';
			}

			if (parts.length === 1) {
				return parts[0];
			}

			const lastPart = parts.pop();
			return `${parts.join(', ')} and ${lastPart}`;
		}

		return {
			isSessionRunning: false,
			countdownString: formatCountdownString(days, hours, minutes)
		};
	}

	/** @type {NodeJS.Timeout | null} */
	let intervalId = null;
	let time = timeUntilNextSession();

	onMount(() => {
		intervalId = setInterval(() => {
			time = timeUntilNextSession();
		}, 1000);
	});

	onDestroy(() => {
		if (intervalId !== null) {
			clearInterval(intervalId);
		}
	});
</script>

<div class="opacity-50">
	{#if time.isSessionRunning}
		<div>Session is live now.</div>
	{:else}
		<div>
			Next session starts in {time.countdownString}.
		</div>
	{/if}
</div>
