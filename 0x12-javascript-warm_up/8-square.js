#!/usr/bin/node
if (isNaN(parseInt(Number(process.argv[2])))) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < process.argv[2]; i++) {
	for (let j = 0; j < process.argv[2]; j++) {
	    process.stdout.write('X');
	}
	console.log();
    }
}
