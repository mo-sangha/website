<script>
	import Photo from '../../../components/Photo.svelte';
</script>

<div class="h-full w-full flex flex-col gap-8 md:gap-16">
	<h2 class="page-header">Publications</h2>

	<div class="page-content-section gap-6">
		<h3 class="font-display text-2xl">Beyond Recognition: Four Phases of Freedom</h3>
		<div class="bookgrid">
			<Photo src="/book-four-phases.svg" url="https://mo-sangha.github.io/book/book.pdf" />
			<div>
				<p>The complete path to liberation practiced by the Meditation Online sangha.</p>
				<p>
					The text details recognition of the nature of mind, post-recognition, and release into
					complete freedom.
				</p>
				<p>
					<a
						href="https://mo-sangha.github.io/book/book.pdf"
						rel="noopener nofollow noreferrer"
						target="_blank"
						class="link-hover text-secondary"
					>
						Freely available as a PDF.
					</a>
				</p>
			</div>
		</div>
	</div>
</div>

<style>
	.bookgrid {
		display: flex;
	}
	.bookgrid div {
		padding-left: 34px;
	}
	.bookgrid p {
		padding-bottom: 10px;
	}
</style>
