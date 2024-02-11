<script lang="ts">
  export let bytes: Uint8Array
  const checkBytes = async (event: Event) => {
    if (bytes) {
      console.log(bytes)
    } else {
      alert("undefined")
    }
  }
</script>

<button class="btn btn-primary" on:click={checkBytes}>Submit</button>
