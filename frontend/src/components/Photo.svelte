<script lang="ts">
	export let src: string;
	export let caption: string;
</script>

<figure class="w-fit">
	<img
		{src}
		alt={caption || src}
		class="max-w-[250px] border-primary shadow-sm shadow-slate-500 border-2"
	/>
	{#if caption}
		<figcaption class="text-center text-sm text-gray-500">{caption}</figcaption>
	{/if}
</figure>
