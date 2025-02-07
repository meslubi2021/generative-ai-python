
# google.generativeai.types.AsyncGenerateContentResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L692-L756">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



This is the async version of `genai.GenerateContentResponse`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.AsyncGenerateContentResponse(
    done: bool,
    iterator: (None | Iterable[protos.GenerateContentResponse] | AsyncIterable[protos.
        GenerateContentResponse]),
    result: protos.GenerateContentResponse,
    chunks: (Iterable[protos.GenerateContentResponse] | None) = None
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`candidates`<a id="candidates"></a>

</td>
<td>

The list of candidate responses.

</td>
</tr><tr>
<td>

`parts`<a id="parts"></a>

</td>
<td>

A quick accessor equivalent to `self.candidates[0].content.parts`

</td>
</tr><tr>
<td>

`prompt_feedback`<a id="prompt_feedback"></a>

</td>
<td>



</td>
</tr><tr>
<td>

`text`<a id="text"></a>

</td>
<td>

A quick accessor equivalent to `self.candidates[0].content.parts[0].text`

</td>
</tr><tr>
<td>

`usage_metadata`<a id="usage_metadata"></a>

</td>
<td>



</td>
</tr>
</table>



## Methods

<h3 id="from_aiterator"><code>from_aiterator</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L694-L704">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>from_aiterator(
    iterator
)
</code></pre>




<h3 id="from_response"><code>from_response</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L706-L712">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_response(
    response: protos.GenerateContentResponse
)
</code></pre>




<h3 id="resolve"><code>resolve</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L751-L756">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>resolve()
</code></pre>




<h3 id="to_dict"><code>to_dict</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L405-L415">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_dict()
</code></pre>

Returns the result as a JSON-compatible dict.

Note: This doesn't capture the iterator state when streaming, it only captures the accumulated
`GenerateContentResponse` fields.

```
>>> import json
>>> response = model.generate_content('Hello?')
>>> json.dumps(response.to_dict())
```



