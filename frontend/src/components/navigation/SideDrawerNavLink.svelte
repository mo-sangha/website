<script lang="ts">
	import type { NavLink } from './types';
	import { page } from '$app/stores';
	import './nav-button.css';
	import { isActive } from './nav-utils';

	export let link: NavLink;
	export let onClick: () => void;

	const handleOnclick = (e: Event) => {
		onClick();
	};
</script>

{#if 'children' in link}
	{#each link.children as child}
		<a
			href={child.href}
			class:underline={isActive(child, $page)}
			aria-label="close sidebar"
			on:click={handleOnclick}
			on:touchstart={handleOnclick}
		>
			{link.name} -> {child.name}
		</a>
	{/each}
{:else}
	<a
		href={link.href}
		class=""
		class:underline={isActive(link, $page)}
		aria-label="close sidebar"
		on:click={handleOnclick}
		on:touchstart={handleOnclick}
	>
		{link.name}
	</a>
{/if}
