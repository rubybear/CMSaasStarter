<script lang="ts">
  import AnalyzeDocument from "./analyze_document.svelte"
  import Bytes from "./bytes.svelte"

  export let bytes: Uint8Array

  const handleFileUpload = async (event: Event) => {
    const target = event.target as HTMLInputElement
    const files = target.files

    if (files?.length !== 1) {
      alert("Please select a single PDF or PNG file.")
      return
    }

    const file = files[0]

    if (file.type !== "image/png" && file.type !== "application/pdf") {
      throw new Error("Invalid file type. Please upload a PDF or PNG file.")
    }

    try {
      const arrayBuffer = (await new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.readAsArrayBuffer(file)
        reader.onload = () => {
          if (reader.result instanceof ArrayBuffer) {
            resolve(reader.result)
          } else {
            reject(new Error("Failed to read file as ArrayBuffer"))
          }
        }
        reader.onerror = reject
      })) as ArrayBuffer

      bytes = new Uint8Array(arrayBuffer)
      console.log(bytes)
    } catch (error) {
      console.error("Error in handleFileUpload:", error)
      alert("Error processing file. Please check the console for details.")
    }
  }
</script>

<div class="flex items-center">
  <input
    type="file"
    accept=".pdf, .png"
    class="file-input file-input-bordered w-full max-w-xs mr-4"
    on:change={handleFileUpload}
  />
  {#if bytes}
    <div class="ml-4">
      <AnalyzeDocument {bytes} />
    </div>
  {/if}
</div>
