<script lang="ts">
	import type { NavLink } from './types';
	import { page } from '$app/stores';
	import './nav-button.css';
	import { isActive } from './nav-utils';

	export let link: NavLink;
</script>

{#if 'children' in link}
	{#each link.children as child}
		<a href={child.href} class:underline={isActive(child, $page)}>
			{link.name} -> {child.name}
		</a>
	{/each}
{:else}
	<a href={link.href} class="" class:underline={isActive(link, $page)}>
		{link.name}
	</a>
{/if}
