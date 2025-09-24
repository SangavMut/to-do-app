import { Component, OnInit } from '@angular/core';
import { Task, TaskService } from './task';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './app.html',
  styleUrls: ['./app.scss']
})
export class App implements OnInit {
  tasks: Task[] = [];
  newTask: string = '';
  editingTaskId: number | null = null;
  updatedTask: string = '';
  showNewTaskModal = false;

  constructor(private taskService: TaskService) {}

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks(): void {
    this.taskService.getTasks().subscribe(data => {
      this.tasks = data;
    });
  }

  addTask(): void {
    if (!this.newTask.trim()) return;
    this.taskService.addTask({ task: this.newTask , id: null}).subscribe(() => {
      this.newTask = '';
      this.loadTasks();
      this.showNewTaskModal = false;
    });
  }
  closeNewTaskModal(): void {
  this.newTask = '';
  this.showNewTaskModal = false;
}


  deleteTask(id: number): void {
    this.taskService.deleteTask(id).subscribe(() => {
      this.loadTasks();
    });
  }

  startEditing(task: Task): void {
    this.editingTaskId = task.id;
    this.updatedTask = task.task;
  }

  cancelEditing(): void {
    this.editingTaskId = null;
    this.updatedTask = '';
  }

  saveTask(task: Task): void {
    if (this.updatedTask.trim() !== '') {
      this.taskService.updateTask({ ...task, task: this.updatedTask }).subscribe(() => {
        task.task = this.updatedTask; 
        this.editingTaskId = null;
        this.updatedTask = '';
      });
    }
  }
}
