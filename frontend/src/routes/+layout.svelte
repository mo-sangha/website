<script>
	import '../app.css';
	import { dev } from '$app/environment';
	import { inject } from '@vercel/analytics';

	inject({ mode: dev ? 'development' : 'production' });
</script>

<div class="h-full w-full flex flex-col px-4">
	<!-- Navbar -->
	<div class="navbar bg-base-100">
		<div class="flex-1">
			<a class="text-xl font-bold" href="/">Meditation Online</a>
		</div>
		<div class="flex-none">
			<ul class="menu menu-horizontal px-1">
				<li><a href="/tools">Tools</a></li>
				<li><a href="/about">About</a></li>
			</ul>
		</div>
	</div>

	<!-- Body -->
	<div class="flex-grow">
		<slot />
	</div>
</div>
