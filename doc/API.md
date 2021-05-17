# REST API

## /api/all

### GET

Get list of all tasks.

#### Response

```json
[
  {
    "id": 1,
    "text": "Go to the super market",
    "time": "2021-05-15 18:30:00+00:00",
    "done": false
  },
  {
    "id": 2,
    "text": "Call John",
    "time": "2021-05-16 10:00:00+00:00",
    "done": true
  },
  {
    "id": 3,
    "text": "Visit mom",
    "time": "2021-05-16 14:13:00+00:00",
    "done": false
  }
]
```

## /api/add

### POST

Add task.

#### Request

```json
{
  "text": "new task"
}
```

#### Response

```json
{
  "id": 4
}
```

## /api/<task_id>

### GET

Get task by id.

#### Response

```json
{
  "id": 4,
  "text": "new task",
  "time": "2021-05-16 18:00:00+00:00",
  "done": false
}
```

### PUT

Update task by id.

#### Request

```json
{
  "text": "task updated",
  "done": true
}
```

#### Response

```json
{
  "id": 4,
  "text": "task updated",
  "time": "2021-05-16 18:10:00+00:00",
  "done": true
}
```

### DELETE

Delete task by id.

#### Response

```
deleted
```
