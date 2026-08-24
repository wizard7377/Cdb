Befunge 1d stack -> 2d stack >:()

Opcodes

## Putting you out of your misery

`\` is a line break (yay!)
` ` and tabs are both no ops (and don't take up space) (so you can at least try to format your code :p)

## Utility

## Information

`{` ... `}` psuedo-opcode writes the stack to the given sub-program
`[` ... `]` writes the string (with proper calls)

`r` takes one arguement and does nothing with it (but sets the accumulator to it) (mnumenoic, read)
`w` puts the value of the accumulator into the stack at the given point

## Movement

### Regular

`←↓↑->`
`|` is the unconditional mirror

#### Condtionals

### Stack

`⇐⇑⇓⇒`

In addition, `~` causes the stack pointer to move in whatever direction it was going in, so `⇒~⇐` (from ltr) is set stack dir right, move one foward, then set the direction back to backwards

Just to be extra confusing, operations go in the order the stack is currently going
