<script lang="ts">
	import '../app.css';
	import { dev } from '$app/environment';
	import { inject } from '@vercel/analytics';
	import Navigation from '../components/navigation/Navigation.svelte';
	import type { NavLink } from '../components/navigation/types';

	const links: NavLink[] = [
		{ name: 'Home', href: '/' },
		{
			name: 'About',
			children: [
				{ name: 'Dawai Gocha', href: '/about/dawai-gocha' },
				{ name: 'Our Lineage', href: '/about/our-lineage' },
				{ name: 'Our Group', href: '/about/our-group' }
			]
		}
	];

	inject({ mode: dev ? 'development' : 'production' });
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
		<nav class="flex flex-row gap-8">
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
			<div class="flex flex-col">
				<header class="footer-title">Socials</header>
				<a href="https://www.youtube.com/@JoinMeditationOnline" class="link link-hover">YouTube</a>
			</div>
		</nav>
	</footer>
</div>
