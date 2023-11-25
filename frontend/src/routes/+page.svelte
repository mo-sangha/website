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

	let isRunning = $state(false);

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

<div>
	{#if isRunning}
		<!-- a button that says start -->
		<div>{slogan.slogan}</div>
		<div>{slogan.chapterTitle}</div>
		<button on:click={() => stopSession()}>Stop</button>
	{:else}
		<button on:click={() => startSession()}>Start</button>
	{/if}
</div>

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.gray.100);
	}
</style>
