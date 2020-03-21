# Terraform::Google::ComputeBackendService CdnPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#signedurlcachemaxagesec" title="SignedUrlCacheMaxAgeSec">SignedUrlCacheMaxAgeSec</a>" : <i>Double</i>,
    "<a href="#cachekeypolicy" title="CacheKeyPolicy">CacheKeyPolicy</a>" : <i>[ <a href="cdnpolicy-cachekeypolicy.md">CacheKeyPolicy</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#signedurlcachemaxagesec" title="SignedUrlCacheMaxAgeSec">SignedUrlCacheMaxAgeSec</a>: <i>Double</i>
<a href="#cachekeypolicy" title="CacheKeyPolicy">CacheKeyPolicy</a>: <i>
      - <a href="cdnpolicy-cachekeypolicy.md">CacheKeyPolicy</a></i>
</pre>

## Properties

#### SignedUrlCacheMaxAgeSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheKeyPolicy

_Required_: No

_Type_: List of <a href="cdnpolicy-cachekeypolicy.md">CacheKeyPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
