import { TestBed } from '@angular/core/testing';

import { WorkexpService } from './workexp.service';

describe('WorkexpService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: WorkexpService = TestBed.get(WorkexpService);
    expect(service).toBeTruthy();
  });
});
