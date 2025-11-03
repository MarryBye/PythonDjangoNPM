export class TestModule {
    testModuleName: string[10];
    someValue: number;

    constructor(testModuleName: string) {
        this.testModuleName = testModuleName;
        this.someValue = 0;
    }

    greet(): void {
        console.log("Hello World!");
    }
}