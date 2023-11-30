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
	let pageDuration = $state(60);
	let slogan = $state(getRandomSlogan());

	function goFullScreen() {
		const elem = document.documentElement;
		if (elem.requestFullscreen) {
			elem.requestFullscreen();
			// @ts-expect-error - typescript doesn't know about requestFullscreen
		} else if (elem.webkitRequestFullscreen) {
			/* Safari */
			// @ts-expect-error - typescript doesn't know about requestFullscreen
			elem.webkitRequestFullscreen();
			// @ts-expect-error - typescript doesn't know about requestFullscreen
		} else if (elem.msRequestFullscreen) {
			/* IE11 */
			// @ts-expect-error - typescript doesn't know about requestFullscreen
			elem.msRequestFullscreen();
		}
	}

	function stopFullScreen() {
		if (document.exitFullscreen) {
			document.exitFullscreen();
			// @ts-expect-error - typescript doesn't know about exitFullscreen
		} else if (document.webkitExitFullscreen) {
			/* Safari */
			// @ts-expect-error - typescript doesn't know about exitFullscreen
			document.webkitExitFullscreen();
			// @ts-expect-error - typescript doesn't know about exitFullscreen
		} else if (document.msExitFullscreen) {
			/* IE11 */
			// @ts-expect-error - typescript doesn't know about exitFullscreen
			document.msExitFullscreen();
		}
	}

	function startSession() {
		goFullScreen();
		isRunning = true;

		// @ts-expect-error - typescript doesn't know about setInterval
		sloganInterval = setInterval(() => {
			slogan = getRandomSlogan();
		}, pageDuration * 1000);
		slogan = getRandomSlogan();
	}

	function stopSession() {
		stopFullScreen();
		clearInterval(sloganInterval);
		isRunning = false;
	}
</script>

<div class="flex flex-col h-full w-full justify-around items-center p-12">
	<div class="flex flex-col max-w-5xl gap-4">
		{#if isRunning}
			<div class="text-2xl sm:text-3xl md:text-4xl lg:text-4xl text-primary">{slogan.slogan}</div>
			<div class="italic opacity-50">{slogan.chapterTitle}</div>
			<button class="btn btn-ghost w-fit opacity-40" on:click={() => stopSession()}>Stop</button>
		{:else}
			<div class="text-4xl text-primary">Lojong Timer</div>
			<p>A simple timer that displays Lojong slogans.</p>
			<div class="flex flex-col gap-4">
				<button class="btn btn-primary w-fit" on:click={() => startSession()}> Start </button>
				<!-- a numeric input to select seconds of practice -->
				<div>
					<label for="step-duration" class="label"> Duration (Seconds) </label>
					<input
						class="input input-md"
						id="step-duration"
						name="step-duration"
						type="number"
						min="1"
						bind:value={pageDuration}
					/>
				</div>
			</div>
		{/if}
	</div>
</div>

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.gray.100);
	}
</style>
