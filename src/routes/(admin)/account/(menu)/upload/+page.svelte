<script lang="ts">
  import type { PageData } from "./$types"

  export let data: PageData
  let { supabase, session, profile } = data
  import { createEventDispatcher } from "svelte"

  const dispatch = createEventDispatcher()
  let file: File | null = null
  let uploadStatus: "idle" | "uploading" | "success" | "error" = "idle"
  let errorMessage: string | null = null

  const handleFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement
    file = target.files ? target.files[0] : null
  }

  const uploadFile = async () => {
    if (!file) {
      errorMessage = "Please select a file."
      return
    }

    try {
      uploadStatus = "uploading"
      const { data, error } = await supabase.storage
        .from("user_forms")
        .upload(session?.user.id + "/" + Date.now() + "/" + file.name, file)

      if (error) {
        throw error
      }

      uploadStatus = "success"
      dispatch("uploadSuccess", data) // Dispatch an event on success
    } catch (error) {
      uploadStatus = "error"
      errorMessage = "Upload failed: " + error
      console.error(error)
    } finally {
      file = null // Clear file selection
    }
  }
</script>

<div class="flex items-center justify-center h-screen">
  <div class="flex items-center">
    <input
      type="file"
      on:change={handleFileChange}
      class="file-input file-input-bordered w-full max-w-xs mr-4"
    />

    {#if file}
      <div>
        <button
          on:click={uploadFile}
          disabled={uploadStatus === "uploading"}
          class="btn btn-primary"
        >
          {#if uploadStatus === "uploading"}
            Uploading...
            <span class="loading loading-ring loading-lg"></span>
          {:else}
            Upload
          {/if}
        </button>
      </div>
    {/if}

    {#if uploadStatus === "success"}
      <div>
        <div role="alert" class="alert alert-success">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="stroke-current shrink-0 h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            ><path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
            /></svg
          >
          <span>Upload successful</span>
        </div>
      </div>
    {:else if uploadStatus === "error"}
      <div>
        <div role="alert" class="alert alert-error">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="stroke-current shrink-0 h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            ><path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
            /></svg
          >
          <span>{errorMessage}</span>
        </div>
      </div>
    {/if}
  </div>
</div>
