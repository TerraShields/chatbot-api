## TerraShields Chat Bot API

### NOTE

- all url need Bearer token

### BASE URL

- https://chat-api-tpercgplna-et.a.run.app/

#### Post Chat Bot

```http
  POST {{url}}/api/chat
```

| Parameter | Type     | Description   |
| :-------- | :------- | :------------ |
| `caption` | `string` | **Required**. |

- success return body

```json
{
	"system": "string"
}
```
