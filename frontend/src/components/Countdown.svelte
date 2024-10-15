<script>
	import { format, addDays, addHours } from 'date-fns';
	import { zonedTimeToUtc, utcToZonedTime } from 'date-fns-tz';
	import { onDestroy, onMount } from 'svelte';

	/**
	 * @returns {{ isSessionRunning: true } | {isSessionRunning: false, clockValues: { hours: number, minutes: number }, labelValues: { hours: string, minutes: string }}
	 */
	function timeUntilNextSession() {
		const now = new Date();
		const TIMEZONE = 'America/New_York';

		// Convert local time to Eastern Time (ET)
		const etTime = utcToZonedTime(now, TIMEZONE);

		// Define session start times
		let morningSession = new Date(format(etTime, 'yyyy-MM-dd') + 'T09:00:00');
		morningSession = zonedTimeToUtc(morningSession, TIMEZONE);

		let eveningSession = new Date(format(etTime, 'yyyy-MM-dd') + 'T21:00:00');
		eveningSession = zonedTimeToUtc(eveningSession, TIMEZONE);

		// Adjust for next day if current time is past 9 PM ET
		if (etTime.getHours() >= 21) {
			morningSession = addDays(morningSession, 1);
		}

		/** @type {number } - the time until the next session */
		let timeUntilNext;

		// Check if the session is running right now
		const isInMorningSession = etTime >= morningSession && etTime < addHours(morningSession, 1);
		const isInEveningSession = etTime >= eveningSession && etTime < addHours(eveningSession, 1);

		if (isInMorningSession || isInEveningSession) {
			return {
				isSessionRunning: true
			};
		}

		if (now < morningSession) {
			timeUntilNext = morningSession.getTime() - now.getTime();
		} else if (now >= morningSession && now < eveningSession) {
			timeUntilNext = eveningSession.getTime() - now.getTime();
		} else {
			timeUntilNext = addDays(morningSession, 1).getTime() - now.getTime();
		}

		// Convert to hours, minutes, and seconds
		const hours = Math.floor(timeUntilNext / (1000 * 60 * 60));
		const minutes = Math.floor((timeUntilNext % (1000 * 60 * 60)) / (1000 * 60));

		return {
			isSessionRunning: false,
			clockValues: {
				hours,
				minutes
			},
			labelValues: {
				hours: hours === 1 ? 'hour' : 'hours',
				minutes: minutes === 1 ? 'minute' : 'minutes'
			}
		};
	}

	/** @type {NodeJS.Timeout | null} */
	let intervalId = $state(null);
	let time = $state(timeUntilNextSession());

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
			Next session starts in {time.clockValues.hours}
			{time.labelValues.hours} and {time.clockValues.minutes}
			{time.labelValues.minutes}.
		</div>
	{/if}
</div>
