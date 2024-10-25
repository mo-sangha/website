<script lang="ts">
import { faChevronRight } from '@fortawesome/free-solid-svg-icons';
import Icon from '../components/Icon.svelte';
import { onMount } from 'svelte';
import iconSmall from '../lib/icon-small.png';

let isLoaded = false;

onMount(() => {
    const img = new Image();
    img.src = iconSmall;
    img.onload = () => {
        isLoaded = true;
    };
});
</script>

{#if !isLoaded}
    <div 
        class="w-[200px] h-[3.75rem] 
               bg-primary/30 rounded-md animate-pulse 
               mx-auto inline-flex"
    ></div>
{:else}
    <a
        href="https://www.paypal.com/paypalme/dawaigocha"
        target="_blank"
        class="relative flex items-center gap-2 w-fit pl-16 pr-5 py-3 
               text-lg font-bold text-primary-content hover:text-white
               bg-primary rounded-md border border-neutral-700
               shadow-md shadow-slate-950/30 hover:shadow-slate-950/50
               fill-primary-content hover:fill-white
               hover:scale-105 transition-all duration-300"
        style="background-image: url({iconSmall}); 
               background-size: 65px 65px; 
               background-position: -16px center; 
               background-repeat: no-repeat;"
    >
        <span class="z-10 pl-1">GIVE DANA</span>
        <Icon icon={faChevronRight} class="z-10" dimension="0.9rem" />
    </a>
{/if}