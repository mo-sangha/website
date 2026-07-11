<script>
	import Photo from '../../../components/Photo.svelte';
	import DonateButton from '/src/components/DonateButton.svelte';
	import DonateButtonKofi from '/src/components/DonateButtonKofi.svelte';
</script>

<div class="h-full w-full flex flex-col gap-8 md:gap-16">
	<h2 class="page-header">Making a Profound Connection</h2>
	<div class="page-content-section">
		<p>
			We will always give these teachings as a gift. If you feel like giving a gift in return, then
			it's considered a profound connection.
		</p>
		<p>
			<a href="/about/lama-dawai-gocha" class="link link-hover text-secondary">Lama Dawai</a>
			and the group will never ask for donations or advertise the group in any way. This means that people
			naturally find the group and naturally discover this offering page, which in turn reflects your
			genuine kindness.
		</p>
		<p>So thank you. May you truly be free.</p>
		<p class="flex justify-center">
			<DonateButton />
			&nbsp;&nbsp;&nbsp;
			<DonateButtonKofi />
		</p>
	</div>
</div>
