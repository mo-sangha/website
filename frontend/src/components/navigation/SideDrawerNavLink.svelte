<script lang="ts">
	import type { NavLink } from './types';
	import { page } from '$app/stores';
	import './nav-button.css';
	import { isActive } from './nav-utils';

	export let link: NavLink;
</script>

{#if 'children' in link}
	<div class="">
		{link.name}
	</div>
	<div class="flex flex-col gap-3">
		{#each link.children as child}
			<a href={child.href}>
				{child.name}
			</a>
		{/each}
	</div>
{:else}
	<a href={link.href} class="" class:underline={isActive(link, $page)}>
		{link.name}
	</a>
{/if}
