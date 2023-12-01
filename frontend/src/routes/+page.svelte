<script>
	import Countdown from '../components/countdown.svelte';
</script>

<div class="hero min-h-[50vh] bg-primary bg-opacity-10">
	<div class="hero-content text-center">
		<div class="max-w-md flex flex-col gap-4">
			<h1 class="text-4xl font-bold">Live Meditation Sessions</h1>
			<div class="text-left mx-auto w-fit">
				<ul class="list-disc">
					<li>Free to join online. All are welcome.</li>
					<li>Twice a day: 9am and 9pm ET.</li>
					<li>Led by Lama Dawai Gocha.</li>
					<li>Established 2013.</li>
				</ul>
			</div>
			<a href="/get-started" class="btn btn-primary">Click here to get started</a>
			<Countdown />
		</div>
	</div>
</div>
