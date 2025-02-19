# Christian Gonzalez

Hello, my name is Christian and I'm a senior at BU. My current favorite programming language is TypeScript, because I love to write type-safe code.

## Example Code

```typescript
interface Friend {
    name: string;
    age: number;
    number: string;
}

const friend: Friend = {
    name: "Sarah",
    age: 21,
    number: "425-523-7890",
}

console.log(friend);
```

### Code Explanation

This TypeScript snippet defines an interface for a friend object. It then creates a friend object and logs it to the console.

To run this code, copy it to a `friend.ts` file and then use the following command:

```bash
tsc friend.ts
node friend.js
```

