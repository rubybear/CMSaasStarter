<script lang="ts">
</script>

<svelte:head>
  <title>Extract</title>
  <meta name="description" content="Upload a file and tigger an extract" />
</svelte:head>

<div
  class="min-h-screen pb-8 pt-20 px-6 flex flex-col items-center justify-center"
>
  <h1 class="text-3xl font-bold text-center">Upload a form</h1>
  <h2 class="text-xl text-center text-slate-500 mt-1 pb-3">
    Analyze handwriting
  </h2>

  <div class="w-full my-8">
    <div class="flex justify-center gap-4">
      <input
        type="file"
        class="file-input file-input-bordered w-full max-w-xs"
      />
      <button class="btn btn-primary font-bold">Submit</button>
    </div>
  </div>
</div>
