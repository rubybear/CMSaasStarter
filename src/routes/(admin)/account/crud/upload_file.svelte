<script lang="ts">
  import type { PageData } from "./$types"

  export let data: PageData
  let { supabase, session, profile } = data
</script>

<h1>Edit Your Profile</h1>

<p>Logged in as: {session?.user.email}</p>
