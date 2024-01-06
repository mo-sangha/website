<script lang="ts">
	import type { NavLink } from './types';
	import { page } from '$app/stores';
	import './nav-button.css';
	import { isActive } from './nav-utils';

	export let link: NavLink;
</script>

{#if 'children' in link}
	<div class="dropdown">
		<div tabindex="0" role="button" class="nav-button">{link.name}</div>
		<ul tabindex="-1" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52">
			{#each link.children as child}
				<a
					href={child.href}
					class="btn btn-ghost hover:bg-base-300 text-primary btn-sm justify-start"
				>
					{child.name}
				</a>
			{/each}
		</ul>
	</div>
{:else}
	<a href={link.href} class="nav-button" class:text-accent={isActive(link, $page)}>
		{link.name}
	</a>
{/if}
