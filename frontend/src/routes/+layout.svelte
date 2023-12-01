<script>
	import '../app.css';
	import { dev } from '$app/environment';
	import { inject } from '@vercel/analytics';

	inject({ mode: dev ? 'development' : 'production' });
</script>

<div class="h-full w-full flex flex-col">
	<!-- Navbar -->
	<div class="navbar bg-base-100 p-gutter">
		<div class="flex-1">
			<a class="text-xl font-bold" href="/">Meditation Online</a>
		</div>
		<div class="flex-none">
			<ul class="menu menu-horizontal px-1">
				<li><a href="/tools">Tools</a></li>
				<li><a href="/about">About</a></li>
				<li><a href="/join">Join</a></li>
			</ul>
		</div>
	</div>

	<!-- Body -->
	<div class="flex-grow">
		<slot />
	</div>

	<!-- Footer -->
	<footer class="footer p-10 mt-10 bg-neutral text-neutral-content p-gutter">
		<nav>
			<header class="footer-title">Site Map</header>
			<a href="/" class="link link-hover">Home</a>
			<a href="/tools" class="link link-hover">Tools</a>
			<a href="/about" class="link link-hover">About</a>
			<a href="/join" class="link link-hover">Join</a>
		</nav>
	</footer>
</div>
