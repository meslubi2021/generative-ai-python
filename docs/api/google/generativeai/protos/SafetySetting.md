
# google.generativeai.protos.SafetySetting

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/safety.py#L224-L273">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Safety setting, affecting the safety-blocking behavior.

<!-- Placeholder for "Used in" -->

Passing a safety setting for a category changes the allowed
probability that content is blocked.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`category`<a id="category"></a>

</td>
<td>

`google.ai.generativelanguage.HarmCategory`

Required. The category for this setting.

</td>
</tr><tr>
<td>

`threshold`<a id="threshold"></a>

</td>
<td>

`google.ai.generativelanguage.SafetySetting.HarmBlockThreshold`

Required. Controls the probability threshold
at which harm is blocked.

</td>
</tr>
</table>



## Child Classes
[`class HarmBlockThreshold`](../../../google/generativeai/types/HarmBlockThreshold.md)

