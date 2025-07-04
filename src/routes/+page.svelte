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
					class="w-24 md:w-36 lg:w-48 aspect-square max-w-[16rem]"
					alt="Dzogchen Symbol"
					src={iconLarge}
				/>
				<h1 class="text-3xl md:text-3xl lg:text-5xl font-bold font-display">
					Live Meditation Sessions
				</h1>
			</div>
			<div class="text-left mx-auto w-fit">
				<ul class="list-disc">
					<li>Always free. All are welcome.</li>
					<li>Twice a day: 9am and 9pm ET.</li>
					<li>Established 2013.</li>
					<li>
						Under the guidance of <a
							class="link-hover text-secondary"
							href="/about/lama-dawai-gocha">Lama Dawai Gocha</a
						>.
					</li>
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
			<h2 class="text-2xl font-display">Free since 2013</h2>
			<p>
				<a href="/" class="link link-hover text-secondary">MeditationOnline.org</a>
				has been an open meditation group since 2013, totally free of charge. We started off on Reddit's
				<a
					href="https://www.reddit.com/r/Buddhism/"
					target="_blank"
					class="link link-hover text-secondary"
					rel="noopener nofollow noreferrer">/r/Buddhism</a
				> subreddit as "redditations." Our online sessions are safe spaces where you can join us from
				anywhere in the world. There is no expectation of donations or payment of any kind.
			</p>
		</div>
	</div>
</div>
