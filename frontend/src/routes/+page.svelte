<script>
	import Citation from '../components/Citation.svelte';
	import Countdown from '../components/Countdown.svelte';
	import iconLarge from '../lib/icon-large.png';
</script>

<div class="flex flex-col gap-8 w-full h-full justify-center">
	<div
		class="min-h-[50vh] bg-gradient-to-b from-base-300 to-base-100 p-gutter flex flex-col text-center justify-center"
	>
		<div class="flex flex-col gap-4 py-16 items-center">
			<div class="flex flex-col gap-8 items-center">
				<img
					class="w-24 md:w-36 lg:w-48 aspect-square"
					alt="Dzogchen Symbol"
					class="max-w-[16rem]"
					src={iconLarge}
				/>
				<h1 class="text-3xl md:text-3xl lg:text-5xl font-bold font-display">
					Live Meditation Sessions
				</h1>
			</div>
			<div class="text-left mx-auto w-fit">
				<ul class="list-disc">
					<li>Free to join online. All are welcome.</li>
					<li>Twice a day: 9am and 9pm ET.</li>
					<li>Established 2013.</li>
					<li>Led by <a class="link-hover text-secondary" href="/about">dawai</a>.</li>
				</ul>
			</div>
			<a
				href="https://meet.jit.si/MeditationOnline"
				rel="noopener nofollow noreferrer"
				target="_blank"
				class="btn btn-primary w-full max-w-lg">Click here to join</a
			>
			<Countdown />
		</div>
	</div>
	<div class="flex flex-col gap-8 pt-6 pb-20">
		<div class="page-content-section">
			<h2 class="text-2xl font-display">Benefits of Meditation & Mindfulness</h2>
			<p>
				Recent news events have shown that change is the only constant. Meditation and mindfulness
				can offer a helpful way to live with this constant change. <Citation
					href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7287297/">NIH</Citation
				>. Many different researchers have analyzed and summarized the effects of meditation on
				behavior and brain imaging in clinical and non-clinical subjects, and have demonstrated
				significant physical and mental health benefits. <Citation
					href="https://www.mdpi.com/1660-4601/18/24/13150#:~:text=The%20Mindfulness%20journal%20ranked%20first,occurrence%20keywords"
					>MDPI</Citation
				>
			</p>
		</div>
		<div class="page-content-section">
			<h2 class="text-2xl font-display">Our Meditation & Mindfulness Practice</h2>
			<p>
				We use formal meditation practices that come from authentic Buddhist lineage.<Citation
					href="/about"
					isLocal>About</Citation
				> The practices we use include mindfulness of breathing, compassion or loving kindness-focused
				meditation, the use of mantras or phrases as the focus for meditation, and many others. We also
				share readings and knowledge from authentic Buddhist tradition, especially Dzogchen and Vajrayana.
			</p>
		</div>
		<div class="page-content-section">
			<h2 class="text-2xl font-display">Free since 2013</h2>
			<p>
				We have been meditating online since 2013, having started off on Reddit's /r/Buddhism
				subreddit as "redditations." Our online sessions are safe spaces where you can join us from
				anywhere in the world, completely for free. There is no expectation of donations or payment
				of any kind. We are a community of people who are interested in meditation and mindfulness,
				and we're happy to have you join us.
			</p>
		</div>
	</div>
</div>
