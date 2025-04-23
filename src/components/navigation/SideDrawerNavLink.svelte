<script lang="ts">
	import type { NavLink, NavLinkBranch, NavLinkLeaf } from './types';
	import { page } from '$app/stores';
	import './nav-button.css';
	import { isActive } from './nav-utils';

	export let link: NavLink;
	export let onClick: (url: string) => void;

	const handleOnclick = (url: string) => {
		onClick(url);
	};
</script>

{#if link.type === 'branch'}
	{#each link.children as child}
		<a
			href={child.href}
			class:underline={isActive(child, $page)}
			aria-label="close sidebar"
			onclick={() => handleOnclick(child.href)}
		>
			{link.name} -> {child.name}
		</a>
	{/each}
{:else if link.type === 'leaf'}
	<a
		href={link.href}
		onclick={() => handleOnclick((link as NavLinkLeaf).href)}
		class=""
		class:underline={isActive(link, $page)}
	>
		{link.name}
	</a>
{/if}
