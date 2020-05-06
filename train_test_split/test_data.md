## intent:greet
- good evening

## intent:retrieve
- show me the [deployment spec](cluster_element)
- I want to see [all](cluster_element) my contexts
- Can I see the qliksense operator [CRD](cluster_element)
- show me the [custom resource](cluster_element)

## intent:tutorial
- what is a [custom resource] (technology)

## intent:inputKey
- Change attribute [NameSpace](key)
- Change attribute [RotateKeys](key)

## intent:inputValue
- [gcp](value)

## intent:setConfig
- I want to set an attribute in the custom resource
- i want to edit my spec

## intent:doPreflight
- check application before deploying
- check [deployment](preflight) preflight

## intent:goodbye
- bye

## intent:affirm
- yes

## intent:deny
- I don't think so
- don't like that

## intent:bot_challenge
- am I talking to a human?

## synonym:CR
- custom resource
- spec
- qliksense spec
- deployment custom resource
- deployment spec
- cr

## synonym:CRD
- custom resource definition
- Operator CRD
- operator custom resource definition

## synonym:all
- list

## synonym:deployments
- Dep
- Deployment
- deployment
- dep

## regex:value
- (.*?)

## lookup:cluster_element
  data/tests/element.txt
