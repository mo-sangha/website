<script>
	/** @type {{ title: string, description: string, link: string }[]} */
	const tools = [
		{
			title: 'Lojong Timer',
			description:
				'A simple, configurable timer that rotates through Lojong phrases every few seconds. No bells or animations.',
			link: '/tools/lojong-timer'
		}
	];
</script>

<div class="flex flex-col gap-4 p-gutter">
	{#each tools as tool}
		<div class="card outline max-w-xs">
			<div class="card-body">
				<div class="card-title">{tool.title}</div>
				<p>{tool.description}</p>
				<a class="btn btn-sm" href={tool.link}>Go</a>
			</div>
		</div>
	{/each}
</div>
