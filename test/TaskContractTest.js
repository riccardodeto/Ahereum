const { flattenSingleFile } = require("@ethereum-waffle/compiler");
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Task Contract", function () {
    let TaskContract;
    let taskContract;
    let owner;

    const NUM_TOTAL_TASKS = 5;

    let totalTasks;

    beforeEach(async function () {
        TaskContract = await ethers.getContractFactory("TodoContract");
        [owner] = await ethers.getSigners();
        taskContract = await TaskContract.deploy();

        totalTasks = [];

        for (let i = 0; i < NUM_TOTAL_TASKS; i++) {
            let task = {
                'taskText': 'CU',
                'isDeleted': false,
                'arrival': false,
                'departure': false,
                'idCU': 123,
                'idNext': 321,
                'margin': 5,
                'data': 'data',
                'orario': 'ora'
            };
            await taskContract.addTask(task.taskText, task.isDeleted, task.arrival, task.departure, task.idCU, task.idNext, task.margin, task.data, task.orario);
            totalTasks.push(task);
        }
    });

    describe("Add Task", function () {
        it("Should emit add task event", async function () {
            let task = {
                'taskText': 'CU',
                'isDeleted': false,
                'arrival': false,
                'departure': false,
                'idCU': 123,
                'idNext': 321,
                'margin': 5,
                'data': 'data',
                'orario': 'ora'
            };
            await expect(await taskContract.addTask(task.taskText, task.isDeleted, task.arrival, task.departure, task.idCU, task.idNext, task.margin, task.data, task.orario)
            ).to.emit(taskContract, 'AddTask').withArgs(owner.address, NUM_TOTAL_TASKS);
        });
    });

    describe("Get all tasks", function () {
        it("Should return the correct number of total tasks", async function () {
            const tasksFromChain = await taskContract.getMyTasks();
            expect(tasksFromChain.length).to.equal(NUM_TOTAL_TASKS);
        });
    });

    describe("Delete Task", function () {
        it("Should emit deleted task event", async function () {
            const TASK_ID = 0;
            const TASK_DELETED = true;
            await expect(
                taskContract.deleteTask(TASK_ID, TASK_DELETED)
            ).to.emit(
                taskContract, 'DeleteTask'
            ).withArgs(
                TASK_ID, TASK_DELETED
            );
        })
    })
})