<script lang="ts">
  export let bytes: Uint8Array

  import {
    TextractClient,
    AnalyzeDocumentCommand,
  } from "@aws-sdk/client-textract"

  let config = {
    credentials: {
      accessKeyId: "AKIA6A5YN6FCJAVGHEZL",
      secretAccessKey: "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",
    },
    region: "us-east-1",
  }

  let textractDocument

  const handleFormSubmit = async (event: Event) => {
    if (!bytes) {
      alert("Please upload a file first.")
      return
    }

    try {
      const client = new TextractClient(config)
      const input = {
        Document: {
          Bytes: bytes,
        },
        FeatureTypes: ["FORMS" || "TEXT" || "SIGNATURES" || "TABLES"],
      }

      const command = new AnalyzeDocumentCommand(input)
      const response = await client.send(command)
      console.log("Response:", response)
      response?.Blocks?.filter((blocks) => blocks.BlockType == "LINE").map(
        (block) => ({
          lineId: block.Id,
          Text: block.Text,
          Relationships: block.Relationships?.map((r) => [r.Ids, r.Type]),
          Polygon: block.Geometry?.Polygon,
        }),
      )

      const lines = response.Blocks?.filter(
        (blocks) => blocks.BlockType == "LINE",
      ).map((block) => ({
        lineId: block.Id,
        Text: block.Text,
        Relationships: block.Relationships?.map((r) => [r.Ids, r.Type]),
        Polygon: block.Geometry?.Polygon,
      }))

      textractDocument = response
    } catch (error) {
      console.error("Error:", error)
      alert("Error analyzing document. Please try again.")
    }
  }
</script>

<button class="btn btn-primary" on:click={handleFormSubmit}>Submit</button>
