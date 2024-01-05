<script lang="ts">
	import '../app.css';
	import { dev } from '$app/environment';
	import { inject } from '@vercel/analytics';
	import { page } from '$app/stores';

	inject({ mode: dev ? 'development' : 'production' });

	type NavLink = { name: string; href: string };
	const links: NavLink[] = [
		{ name: 'Home', href: '/' },
		// { name: 'Tools', href: '/tools' },
		{ name: 'Lineage', href: '/lineage' },
		{ name: 'About', href: '/about' }
	];
</script>

<div class="h-full w-full flex flex-col justify-between">
	<!-- Navbar -->
	<div class="navbar bg-primary text-primary-content p-gutter">
		<div class="flex-1">
			<a class="text-xl font-bold" href="/">Meditation Online</a>
		</div>
		<!-- full menu -->
		<div class="flex-none flex-row gap-4 hidden lg:flex">
			{#each links as link}
				<a
					href={link.href}
					class="btn btn-sm btn-ghost rounded-btn btn-primary"
					class:text-accent={link.href === $page.url.pathname}
				>
					{link.name}
				</a>
			{/each}
		</div>
		<!-- Drawer -->
		<div class="drawer drawer-end lg:hidden w-fit z-50">
			<input id="meditationonline-nav-drawer" type="checkbox" class="drawer-toggle" />
			<div class="drawer-content">
				<!-- Page content here -->
				<label
					for="meditationonline-nav-drawer"
					class="drawer-button btn btn-accent btn-square btn-sm">☰</label
				>
			</div>
			<div class="drawer-side">
				<label for="meditationonline-nav-drawer" aria-label="close sidebar" class="drawer-overlay"
				></label>
				<ul class="sidebar-list">
					<li class="sidebar-list-item">
						<label for="meditationonline-nav-drawer" aria-label="close sidebar" class="link">
							Close
						</label>
					</li>
					{#each links as link}
						<li class="sidebar-list-item">
							<a href={link.href} class:text-secondary={link.href === $page.url.pathname}>
								{link.name}
							</a>
						</li>
					{/each}
				</ul>
			</div>
		</div>
	</div>

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

<style type="postcss">
	.sidebar-list {
		@apply w-60 min-h-full bg-base-200 text-base-content flex flex-col;
	}
	.sidebar-list-item {
		@apply w-full h-full flex flex-col;
	}

	.sidebar-list-item > * {
		@apply py-3 px-5 w-full h-full hover:bg-base-100 transition-colors duration-300;
	}
</style>
