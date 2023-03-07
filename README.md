# terralibrary

computers are magic.

screens are horrible.

paper is lovely.

books are beautiful.

*terralibrary is a magic screenless computer for a beautiful library.*

## what

- a magic wand (barcode reader)
- a magic brain (raspberry pi)
- a magic mouth (a usb speaker)
- a magic scroll (receipt printer)

## inspo

- [Dynamicland](https://dynamicland.org/)
- [Hypercard In The World](https://tashian.com/articles/dynamicland/)
- [ELECTRONICOS FANTASTICOS!](https://www.electronicosfantasticos.com/)

## setup

Check out [SETUP.md](SETUP.md)

## arguments

- screens are horrible because they demand visual and thus cognitive attention; they lock you into a location and a bodily orientation
- paper is lovely because paper moves around in space; it has spatial affordances, and thus participates in psychospatial life; you can hide tuck fold unfold file page glue stick pin crumple paper. your body moves, too. paper is a read-write medium, easily manipulatible, unprecious and friendly, and most importantly, can move where the body moves.
  -  see: "the myth of the paperless office"
- audio is somatically freeing because your body can be in any position and you can still listen; others can listen, too
- barcode scanners are like magic wands: they engage the body, and it's clear to everyone else what you're doing when you point, too. a barcode scanner with a trigger gives clear vibration/sound feedback of scan success. scanning/magicking becomes a singular and intentional gesture.
- the spoken word is clear
- computers should be weird

## philosophy
- **everything should be hackable.** this is a magic medium, not an interface. a medium is a truly hackable system that you might be able to mess up.
- **let the physical world keep things mysterious.** anything to do with secrecy or authentication should happen through paper. (printed qr code as password, checksum match in order to login)
- **screens do not scroll.** scrolling is a disassociative abomination. text that doesn't fit shrinks to fit the screen.
- **this is not a novelty, but part of real life.** I want to use this on a regular basis; for it to be really meaningful.

## ideas/notes

- 'magic wall' - web interface for editing & printing chunks of code. like dynamicland's operating system wall. if it's a qr code, it's on this wall.

- incantation/command composition
  - google sheets or airtable sheet operation. a barcode command (e.g. `sheet check in 0123456789`) says: in a sheet, corresponds to the column `check` of the row `0123456789`, and that cell being set to `in`. Thus all 'programming' can happen in google sheets, pretty fluidly and user-editable
  - being able to compose and 'save' a stack of commands in prefix/polish notation, since the most common use case will be scanning a whole chunk of books at a time. it would be nice to be able to say `sheet tag--critical-technology-studies x`, save that as a stack, so that subsequent scans will be `sheet tag--critical-technology-studies x 0123456789`
  - being able to 'type' and compose a string via scanning an alphabet, then printing out a barcode/qrcode of that string, so that tags can actually be written 
  - in the above examples, the whole command can be saved as a qr code (since it's just text), so `sheet check in ` as a qr code that can be scanned as an easy 'check in' command
  - how to read? `sheet read check 0123456789` ? 
  - potential placeholders for scan variables. etc. `sheet [VAL] check in`. 
  - or multi-step scanning. perhaps - `sheet tag-[2] x [1]` will create a multi-step scan. scanning '0123456789' and 'cybernetics' will result in the command `sheet tag-cybernetics x 0123456789`, etc.
  - what about a variable for the existing string/stack? e.g. `print [stack]`?  
- undo command?

- clear command structure. 
  - `!!`: system level / debug commands. e.g. `!!reloadbarlanginterpreter`
  - `print!` or `!print` for commands? or `:print` like vim?
  - `@mode`? for a modal system
- is there a distinction between text and commands? maybe the first word is the command? or a command has to be prepended with a `!`?
  - e.g. `print! [string]` or `run! string`
- maybe there is 'assembling a magic incantation' vs 'running it'
  - how do you run the command? 'closing the circle' ala Witch Hat Atelier?
    - incantations are a sequence of commands within a wrapper/parenthesis (faux lisp syntax). e.g. `(say! 0123456)`
    - if the parenthesis isn't closed, the command doesn't run. `(say! hello` doesn't run. scanning `)` will run the command.
    - if the incantation contains a placeholder, the command doesn't run. e.g. `(say! hello, my name is [1])`
    - the metaphor is: incantation is written. when the incantation is complete, it runs and disappears. if it uses a placeholder, it stays fresh for 5 minutes, at which point it disappears.
    - incantations can be assembled in `@write` mode. in this mode, any code scanned just gets added to a buffer.
    - incantations can be cast in `@cast` mode. in this mode, the buffer is either immediately cast or cast as soon as possible. 
    - wrappers are how incantations are versioned. such as `1-(say! hello)-1` or `oO--(say! hello)--Oo` or `x|x|x--(say! hello)--x|x|x`. the closing wrapper can just be `)` but it's kind of fun to have it be the same. 
    - so. for example:
      - I scan `1-(`
      - and then I scan `library_write!`, which takes three arguments: row, column, value
      - and then I scan `{{1}}`, a placeholder
      - and then I scan `checked_in`, and `yes`
      - and then I scan `)-1`
      - the incantation buffer is: `1-(library_write! {{1}} checked_in yes)-1`
      - it doesn't run yet, because we have a placeholder
      - when I scan a barcode `0123456789`, `1-(library_write! 0123456789 checked_in yes)-1` runs
        - which: sets the row of `012345679`, column `checked_in` and sets the value to `yes`
