Befunge 1d stack -> 2d stack >:()

Opcodes

## Putting you out of your misery

`\` is a line break (yay!)
` ` and tabs are both no ops (and don't take up space) (so you can at least try to format your code :p)

## Utility

## Information

`{` ... `}` psuedo-opcode writes the stack to the given sub-program
`[` ... `]` writes the string (with proper calls)

## Movement

### Regular

`←↓↑->`
`⇐⇑⇓⇒`

### Stack

uppercase versions of above for setting stack direction.
In addition, `\` causes the stack pointer to move, and `<` causes the stack pointer to move back
