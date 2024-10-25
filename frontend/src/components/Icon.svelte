<script lang="ts">
	import type { IconDefinition } from '@fortawesome/free-brands-svg-icons';
	export let icon: IconDefinition;
	export let color: string;
	export let dimension: string = '1rem';

	const [width, height, ligatures, unicode, svgPathData] = icon.icon;
</script>

<div class="flex bg-red-50 rounded-full align-middle items-center p-1" {...$$restProps}>
	<svg
		height={dimension}
		width={dimension}
		viewBox={`0 0 ${width} ${height}`}
		xmlns="http://www.w3.org/2000/svg"
	>
		<path fill={color} stroke={color} d={svgPathData as string} />
	</svg>
</div>
