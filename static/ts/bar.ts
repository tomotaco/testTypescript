import $ from "jquery"

export class Bar
{
	val: number;
	constructor(v: number) {
		this.val = v;
	}
	getValue() : number {
		return this.val;
	}
	setValue(v: number): void {
		this.val = v;
	}
}

$("#result2").text("jQuery in bar executed");