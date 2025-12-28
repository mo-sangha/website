<script lang="ts">
	export let src: string;
	export let caption: string | undefined = undefined;
	export let url: string | undefined = undefined;
</script>

<figure class="w-fit">
	{#if url}
		<a href={url} rel="noopener nofollow noreferrer" target="_blank">
			<img
				{src}
				alt={caption || src}
				class="max-w-[250px] border-primary shadow-sm shadow-slate-500 border-2"
			/>
		</a>
	{:else}
		<img
			{src}
			alt={caption || src}
			class="max-w-[250px] border-primary shadow-sm shadow-slate-500 border-2"
		/>
	{/if}
	{#if caption}
		<figcaption class="text-center text-sm text-gray-500">{caption}</figcaption>
	{/if}
</figure>
