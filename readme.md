## TerraShields Chat Bot API

### NOTE

- all url need Bearer token

### BASE URL

-

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
