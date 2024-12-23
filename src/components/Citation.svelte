<script>
	/** @type { string }*/
	export let href;
	export let isLocal = true;
</script>

<a
	{href}
	class="align-super text-[0.75em] link-hover text-secondary"
	rel={isLocal ? '' : 'noopener nofollow noreferrer'}
	target={isLocal ? '_self' : '_blank'}
>
	[<slot />]
</a>
