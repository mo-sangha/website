<script lang="ts">
	import Countdown from '/src/components/Countdown.svelte';
	const meditationEvents = [
		{ title: 'Meditation by Bee', dayOfWeek: 6, times: ['10:00'] },
		{ title: 'Meditation by Bee', dayOfWeek: 0, times: ['10:00'] }
	];

	function twelveHourTime(time: string) {
		const [hours, minutes] = time.split(':').map(Number);
		const ampm = hours >= 12 ? 'pm' : 'am';
		const displayHours = hours % 12 || 12;
		return `${displayHours}:${minutes.toString().padStart(2, '0')} ${ampm}`;
	}

	function namedDayOfWeek(day: number) {
		const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
		return days[day];
	}

	function formatTimes(times: string[]) {
		const items = times.map(twelveHourTime);
		if (items.length === 0) return '';
		if (items.length === 1) return items[0];
		if (items.length === 2) return `${items[0]} and ${items[1]}`;

		const lastItem = items.pop();
		return `${items.join(', ')}, and ${lastItem}`;
	}
</script>

<div class="h-full w-full flex flex-col gap-8 md:gap-16">
	<h2 class="page-header">Meditations by Bee</h2>
	<div class="page-content-section">
		This page offers meditations and guided sits led by practitioners from the Meditation Online
		community. These sessions welcome participants of all experience levels, unless otherwise noted.
		The meditations aim to support your practice by offering a regular opportunity to meditate in a
		group setting. Sessions are free to join and held regularly, making it easy to fit into your
		schedule.
	</div>
	{#each meditationEvents as { title, dayOfWeek, times }}
		<div class="page-content-section flex flex-col items-center text-center gap-4">
			<h3 class="font-display text-2xl">{title}</h3>
			<p>{namedDayOfWeek(dayOfWeek)}s at {formatTimes(times)} EST (USA Eastern time).</p>
			<a href="https://meet.jit.si/meditationhangout" class="btn btn-primary w-fit">Join Room</a>
			<Countdown {dayOfWeek} {times} />
		</div>
	{/each}
</div>
