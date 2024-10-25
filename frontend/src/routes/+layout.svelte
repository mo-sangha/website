<script lang="ts">
	import '../app.css';
	import Navigation from '../components/navigation/Navigation.svelte';
	import { links } from './navLinks';
	import { definition as faDiscord } from '@fortawesome/free-brands-svg-icons/faDiscord';
	import { definition as faYoutube } from '@fortawesome/free-brands-svg-icons/faYoutube';
	import Icon from '../components/Icon.svelte';
	import DonateButton from '../components/DonateButton.svelte';
	

	const socialIcons = [
		{
			icon: faYoutube,
			color: '#CD201F',
			label: 'YouTube',
			href: 'https://www.youtube.com/@JoinMeditationOnline'
		},
		{ icon: faDiscord, color: '#7289da', label: 'Discord', href: 'https://discord.gg/J7NVKYmHNR' }
	];
</script>

<div class="h-full w-full flex flex-col justify-between">
	<!-- Navbar -->
	<Navigation {links} />

	<!-- Body -->
	<div class="flex-grow">
		<slot />
	</div>

	<!-- Footer -->
	<footer
		class="footer p-10 mt-10 bg-gradient-to-b from-base-100 to-base-300 text-neutral-content p-gutter"
	>
		<nav class="flex flex-row justify-between w-full">
			<div class="flex flex-col">
				<header class="footer-title">Site Map</header>
				<!-- <a href="/" class="link link-hover">Home</a>
				<a href="/tools" class="link link-hover">Tools</a>
				<a href="/about" class="link link-hover">About</a> -->

				{#each links as link}
					{#if 'children' in link}
						{#each link.children as child}
							<a href={child.href} class="link link-hover">{link.name} -> {child.name}</a>
						{/each}
					{:else}
						<a href={link.href} class="link link-hover">{link.name}</a>
					{/if}
				{/each}
			</div>
			<div class="flex flex-col gap-2">
				<header class="footer-title">Socials</header>
				{#each socialIcons as def}
					<a
						href={def.href}
						target="_blank"
						class="link link-hover flex flex-row gap-1 align-middle justify-start"
					>
						<Icon icon={def.icon} color={def.color} />
						{def.label}
					</a>
				{/each}
			</div>
			<div class="flex flex-col gap-1">
				<header class="footer-title">Donate</header>
				<DonateButton />
			</div>
		</nav>
	</footer>
</div>
