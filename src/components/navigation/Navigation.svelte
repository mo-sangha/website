<script lang="ts">
	import SideDrawerNavLink from './SideDrawerNavLink.svelte';
	import TopbarNavLink from './TopbarNavLink.svelte';
	import type { NavLink } from './types';
	import { goto } from '$app/navigation';

	export let links: NavLink[];
	let drawerRef: HTMLInputElement;

	const handleNavDrawerItemClicked = (targetUrl: string) => {
		if (drawerRef.checked) {
			drawerRef.checked = false;
		}

		goto(targetUrl);
	};
</script>

<div class="navbar bg-primary text-primary-content p-gutter">
	<a class="text-xl font-bold flex-1 gap-3" href="/"
		><img src="/favicon-32x32.png" alt="" class="inline-block w-fit object-contain h-7" /> Meditation
		Online
	</a>
	<!-- full menu -->
	<div class="flex-none flex-row gap-4 hidden 2xl:flex">
		{#each links as link}
			<TopbarNavLink {link} />
		{/each}
	</div>
	<!-- Drawer -->
	<div class="drawer drawer-end 2xl:hidden w-fit z-50">
		<input
			id="meditationonline-nav-drawer"
			type="checkbox"
			class="drawer-toggle"
			bind:this={drawerRef}
		/>
		<div class="drawer-content">
			<!-- Page content here -->
			<label for="meditationonline-nav-drawer" class="drawer-button nav-button">☰</label>
		</div>
		<div class="drawer-side">
			<label for="meditationonline-nav-drawer" aria-label="close sidebar" class="drawer-overlay"
			></label>
			<ul class="w-60 p-6 min-h-full bg-base-200 text-base-content flex flex-col gap-4">
				<li class="">
					<label for="meditationonline-nav-drawer" aria-label="close sidebar" class="link">
						Close
					</label>
				</li>
				{#each links as link}
					<SideDrawerNavLink {link} onClick={handleNavDrawerItemClicked} />
				{/each}
			</ul>
		</div>
	</div>
</div>
