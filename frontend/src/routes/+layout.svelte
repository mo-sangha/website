<script lang="ts">
	import '../app.css';
	import { dev } from '$app/environment';
	import { inject } from '@vercel/analytics';
	import Navigation from '../components/navigation/Navigation.svelte';

	inject({ mode: dev ? 'development' : 'production' });
</script>

<div class="h-full w-full flex flex-col justify-between">
	<!-- Navbar -->
	<Navigation />

	<!-- Body -->
	<div class="flex-grow">
		<slot />
	</div>

	<!-- Footer -->
	<footer
		class="footer p-10 mt-10 bg-gradient-to-b from-base-100 to-base-300 text-neutral-content p-gutter"
	>
		<nav>
			<header class="footer-title">Site Map</header>
			<a href="/" class="link link-hover">Home</a>
			<!-- <a href="/tools" class="link link-hover">Tools</a> -->
			<a href="/about" class="link link-hover">About</a>
		</nav>
	</footer>
</div>
