<script>
	import * as lojong from '$lib/lojong';

	/**
	 * Pick a random item from an array
	 * @template T
	 * @param {T[]} array - the array to pick from
	 * @returns {T} a random item from the array
	 */
	const pickRandom = (array) => {
		const randomIndex = Math.floor(Math.random() * array.length);
		return array[randomIndex];
	};

	const getRandomSlogan = () => {
		const chapter = pickRandom(lojong.slogans);
		const chapterTitle = chapter.title;
		const slogan = pickRandom(chapter.slogans);
		return { chapterTitle, slogan };
	};

	let isRunning = $state(true);

	let sloganInterval = $state(0);
	let slogan = $state(getRandomSlogan());

	function startSession() {
		isRunning = true;

		// @ts-expect-error - typescript doesn't know about setInterval
		sloganInterval = setInterval(() => {
			slogan = getRandomSlogan();
		}, 5 * 1000);
		slogan = getRandomSlogan();
	}

	function stopSession() {
		clearInterval(sloganInterval);
		isRunning = false;
	}
</script>

<div class="flex flex-col h-full w-full justify-around items-center p-12">
	<div class="flex flex-col max-w-5xl gap-4">
		{#if isRunning}
			<div class="text-2xl sm:text-3xl md:text-4xl lg:text-4xl text-primary">{slogan.slogan}</div>
			<div class="italic opacity-40">{slogan.chapterTitle}</div>
			<button class="btn btn-ghost w-fit opacity-40" on:click={() => stopSession()}>Stop</button>
		{:else}
			<div class="text-4xl">Lojong Timer</div>
			<button class="btn btn-primary w-fit" on:click={() => startSession()}> Start </button>
		{/if}
	</div>
</div>

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.gray.100);
	}
</style>
