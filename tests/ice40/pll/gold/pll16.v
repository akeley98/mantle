module main (output  O, input  CLKIN);
wire  inst0_PLLOUTCORE;
wire  inst0_PLLOUTGLOBAL;
SB_PLL40_CORE #(.FEEDBACK_PATH("SIMPLE"),
.DIVF(7'b0101100),
.FILTER_RANGE(3'b001),
.PLLOUT_SELECT("GENCLK"),
.DIVR(4'b0000),
.DIVQ(3'b101)) inst0 (.REFERENCECLK(CLKIN), .RESETB(1'b1), .BYPASS(1'b0), .PLLOUTCORE(inst0_PLLOUTCORE), .PLLOUTGLOBAL(inst0_PLLOUTGLOBAL));
assign O = inst0_PLLOUTGLOBAL;
endmodule
