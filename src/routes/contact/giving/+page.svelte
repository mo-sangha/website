<script>
	import Photo from '../../../components/Photo.svelte';
	import DonateButton from '/src/components/DonateButton.svelte';
	import DonateButtonKofi from '/src/components/DonateButtonKofi.svelte';
</script>

<div class="h-full w-full flex flex-col gap-8 md:gap-16">
	<h2 class="page-header">Giving (Dana) in Buddhist Practice</h2>
	<div class="page-content-section">
		<p>
			In Buddhism, Dana (generosity) is a practice of profound significance, embodying the essence
			of non-dual awareness. It goes beyond mere giving; it's an expression of interconnectedness
			and compassion. This practice helps to dissolve the ego, fostering a heart of openness and
			compassion. Your Dana directly aids the dissemination of Dzogchen teachings and sustains our
			community. Each act of generosity, big or small, contributes to the growth and vitality of our
			spiritual family.
		</p>
		<p class="flex justify-center">
			<DonateButton />
		</p>
		<p class="flex justify-center">
			<DonateButtonKofi />
		</p>
		<p>
			Dana given to the Meditation Online community offers vital support to <a
				href="/about/lama-dawai-gocha"
				class="link link-hover text-secondary">Lama Dawai Gocha</a
			>. Having vowed to always give Dharma as a gift, your generosity helps sustain his daily needs
			but also helps many other beings. Please know he is deeply grateful for the connection and
			support, all help ultimately benefits the spread of meditation and a path to true freedom of
			mind.
		</p>
		<div class="flex flex-col gap-4">
			<div class="font-display text-2xl">How to give Dana to Meditation Online.</div>

			<div class="flex flex-col xl:flex-row-reverse 2xl:justify-end gap-4">
				<div class="flex flex-col h-full gap-2">
					<p>
						Thank you for your generosity in considering Dana for Meditation Online. Meditation
						Online is for the benefit of all sentient beings and will remain free regardless of
						donation provided.
					</p>
					<ul class="list-disc flex flex-col md:pl-6">
						<li>No donation is required or mandatory.</li>
						<li>
							Funds are used for the group's Dharma activities and Lama Dawai's living expenses.
						</li>
					</ul>
				</div>
				<Photo src="/photo-begging-bowl.jpg" />
			</div>
		</div>
	</div>
</div>
