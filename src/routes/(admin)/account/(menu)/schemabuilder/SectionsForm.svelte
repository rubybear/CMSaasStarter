<!-- src/routes/index.svelte -->
<script lang="ts">
  import { writable } from "svelte/store"

  // Define interfaces
  interface Fields {
    fieldName: string
    description: string
  }

  interface Section {
    name: string
    fields: Fields[]
    newFieldName: string
    newFieldDescription: string
  }

  interface Document {
    id: string
    sections: Section[]
  }

  // Store for sections
  const sections = writable<Section[]>([])

  // Variables for new section
  let newSectionName = ""

  // Add a new section
  function addSection() {
    if (newSectionName.trim() === "") {
      return // Do not add section if name is empty
    }

    sections.update((currentSections) => [
      ...currentSections,
      {
        name: newSectionName,
        fields: [],
        newFieldName: "",
        newFieldDescription: "",
      },
    ])
    newSectionName = ""
  }

  // Add a new field to a section
  function addField(sectionIndex: number) {
    const sectionToUpdate = $sections[sectionIndex]
    if (sectionToUpdate.newFieldName.trim() === "") {
      return
    }
    const camelCaseFieldName = sectionToUpdate.newFieldName
      .toLowerCase()
      .split(" ")
      .map((word, index) => {
        if (index === 0) {
          return word
        } else {
          return word.charAt(0).toUpperCase() + word.slice(1)
        }
      })
      .join("")

    sections.update((currentSections) => {
      const updatedSections = [...currentSections]
      updatedSections[sectionIndex].fields.push({
        fieldName: camelCaseFieldName,
        description: sectionToUpdate.newFieldDescription,
      })
      updatedSections[sectionIndex].newFieldName = ""
      updatedSections[sectionIndex].newFieldDescription = ""
      return updatedSections
    })
  }

  // Submit sections data
  function submitData() {
    sections.subscribe((data) => {
      const document: Document = {
        id: "some_unique_id_here",
        sections: data,
      }
      console.log("Submitted data:", document)
    })
  }
</script>

<div>
  <!-- Input for new section -->
  <div>
    <h3>Sections</h3>
    <div class="flex space-x-2">
      <input
        class="input input-bordered input-sm max-w-xs"
        type="text"
        bind:value={newSectionName}
        placeholder="Enter section name"
      />
      <button class="btn btn-outline btn-accent btn-sm" on:click={addSection}
        >Add Section</button
      >
    </div>
  </div>

  {#each $sections as section, sectionIndex}
    <div class="mt-2">
      <h3>{section.name}</h3>
      <!-- Input for new field -->
      {#each section.fields as field, fieldIndex}
        <div class="flex space-x-2" key={fieldIndex}>
          <input
            class="input input-bordered input-sm max-w-xs"
            type="text"
            bind:value={section.fields[fieldIndex].fieldName}
            placeholder="Enter field name"
          />
          <input
            class="input input-bordered input-sm max-w-xs"
            type="text"
            bind:value={section.fields[fieldIndex].description}
            placeholder="Enter field description"
          />
          <button
            class="btn btn-outline btn-accent btn-sm"
            on:click={() => addField(sectionIndex)}>Add Field</button
          >
        </div>
      {/each}
      <div class="flex space-x-2 mt-2">
        <input
          class="input input-bordered input-sm max-w-xs"
          type="text"
          bind:value={section.newFieldName}
          placeholder="Enter field name"
        />
        <input
          class="input input-bordered input-sm max-w-xs"
          type="text"
          bind:value={section.newFieldDescription}
          placeholder="Enter field description"
        />
        <button
          class="btn btn-outline btn-accent btn-sm"
          on:click={() => addField(sectionIndex)}>Add Field</button
        >
      </div>
    </div>
  {/each}
</div>

{#if $sections.length > 0 && $sections[0].fields.length > 0}
  <button class="btn btn-primary btn-sm" on:click={submitData}>Submit</button>
{/if}
